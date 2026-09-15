$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$port = 8000
$url = "http://localhost:$port/industry-intelligence/oil-gas-ai-lab/"

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

$listener = [Net.HttpListener]::new()
$listener.Prefixes.Add("http://localhost:$port/")
try { $listener.Start() } catch {
  Write-Host "Port $port is unavailable. Close any existing local preview and try again."
  exit 1
}
Write-Host ""
Write-Host "SOUBEL Oil & Gas AI Lab local preview"
Write-Host "Opening $url"
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
