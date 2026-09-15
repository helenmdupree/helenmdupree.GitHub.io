$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot

function Get-ContentType([string]$path) {
  switch ([IO.Path]::GetExtension($path).ToLowerInvariant()) {
    ".html" { "text/html; charset=utf-8" }
    ".css"  { "text/css; charset=utf-8" }
    ".js"   { "application/javascript; charset=utf-8" }
    ".json" { "application/json; charset=utf-8" }
    ".png"  { "image/png" }
    ".jpg"  { "image/jpeg" }
    ".jpeg" { "image/jpeg" }
    ".svg"  { "image/svg+xml" }
    ".ico"  { "image/x-icon" }
    ".webp" { "image/webp" }
    default { "application/octet-stream" }
  }
}

$listener = $null
$port = $null
foreach ($candidatePort in 8000..8010) {
  $candidateListener = [Net.HttpListener]::new()
  $candidateListener.Prefixes.Add("http://localhost:$candidatePort/")
  try {
    $candidateListener.Start()
    $listener = $candidateListener
    $port = $candidatePort
    break
  } catch {
    try { $candidateListener.Close() } catch {}
  }
}

if (-not $listener) {
  Write-Host "No available local preview port was found between 8000 and 8010."
  exit 1
}

$url = "http://localhost:$port/industry-intelligence/oil-gas-ai-lab/"
Write-Host ""
Write-Host "SOUBEL Oil & Gas AI Lab local preview"
Write-Host "Opening $url"
if ($port -ne 8000) {
  Write-Host "Port 8000 was already in use, so the preview selected port $port instead."
}
Write-Host "Leave this window open while reviewing. Press Ctrl+C to stop."
Start-Process $url

while ($listener.IsListening) {
  $context = $listener.GetContext()
  try {
    $relative = [Uri]::UnescapeDataString($context.Request.Url.AbsolutePath.TrimStart("/"))
    if ([string]::IsNullOrWhiteSpace($relative)) { $relative = "index.html" }
    $candidate = Join-Path $root ($relative -replace "/", "\")
    if (Test-Path $candidate -PathType Container) { $candidate = Join-Path $candidate "index.html" }
    $full = [IO.Path]::GetFullPath($candidate)
    $rootFull = [IO.Path]::GetFullPath($root)
    if (-not $full.StartsWith($rootFull, [StringComparison]::OrdinalIgnoreCase)) {
      $context.Response.StatusCode = 403
    } elseif (Test-Path $full -PathType Leaf) {
      $bytes = [IO.File]::ReadAllBytes($full)
      $context.Response.ContentType = Get-ContentType $full
      $context.Response.ContentLength64 = $bytes.Length
      $context.Response.OutputStream.Write($bytes,0,$bytes.Length)
    } else {
      $context.Response.StatusCode = 404
    }
  } catch {
    $context.Response.StatusCode = 500
  } finally {
    $context.Response.OutputStream.Close()
  }
}
