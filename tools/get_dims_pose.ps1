Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('assets/pose_1.png')
Write-Output "Width: $($img.Width) Height: $($img.Height)"
$img.Dispose()
