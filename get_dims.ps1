Add-Type -AssemblyName System.Drawing
$img = [System.Drawing.Image]::FromFile('assets/pradeep_sheet.png')
Write-Output "Width: $($img.Width) Height: $($img.Height)"
$img.Dispose()
