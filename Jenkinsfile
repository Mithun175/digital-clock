
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Deploy Clock') {
            steps {
                powershell '''
                    $folder = "C:\\DigitalClockSite"
                    New-Item -ItemType Directory -Force -Path $folder | Out-Null
                    Copy-Item "$env:WORKSPACE\\index.html" $folder -Force
                    Copy-Item "$env:WORKSPACE\\style.css" $folder -Force
                    Write-Output "Clock files copied successfully"
                '''
            }
        }

        stage('Start Local Website') {
            steps {
                powershell '''
                    $port = 8000
                    $listener = [System.Net.Sockets.TcpListener]::new(
                        [System.Net.IPAddress]::Loopback, $port
                    )
                    try {
                        $listener.Start()
                        $listener.Stop()
                        $listener = $null
                    } catch {
                        if ($listener) { $listener.Stop() }
                        Write-Output "Port 8000 may already be in use."
                    }

                    $folder = "C:\\DigitalClockSite"
                    $script = @"
                    `$listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Loopback, 8000)
                    `$listener.Start()
                    while (`$true) {
                        `$client = `$listener.AcceptTcpClient()
                        `$stream = `$client.GetStream()
                        `$reader = [System.IO.StreamReader]::new(`$stream)
                        `$request = `$reader.ReadLine()
                        while (`$reader.ReadLine() -ne '') {}
                        `$path = Join-Path '$folder' 'index.html'
                        if (`$request -match '^GET /style.css ') {
                            `$path = Join-Path '$folder' 'style.css'
                            `$type = 'text/css'
                        } else {
                            `$type = 'text/html'
                        }
                        `$bytes = [System.IO.File]::ReadAllBytes(`$path)
                        `$header = "HTTP/1.1 200 OK`r`nContent-Type: `$type; charset=utf-8`r`nContent-Length: `$(`$bytes.Length)`r`nConnection: close`r`n`r`n"
                        `$headBytes = [System.Text.Encoding]::ASCII.GetBytes(`$header)
                        `$stream.Write(`$headBytes, 0, `$headBytes.Length)
                        `$stream.Write(`$bytes, 0, `$bytes.Length)
                        `$client.Close()
                    }
"@
                    $scriptPath = Join-Path $folder "server.ps1"
                    Set-Content -Path $scriptPath -Value $script
                    $existing = Get-NetTCPConnection -LocalPort $port -State Listen -ErrorAction SilentlyContinue
                    if (-not $existing) {
                        Start-Process powershell.exe -ArgumentList @(
                            '-NoProfile', '-ExecutionPolicy', 'Bypass',
                            '-File', $scriptPath
                        ) -WindowStyle Hidden
                    }
                    Start-Sleep -Seconds 2
                    Invoke-WebRequest "http://localhost:8000" -UseBasicParsing | Out-Null
                    Write-Output "Clock website is running at http://localhost:8000"
                '''
            }
        }
    }
}
