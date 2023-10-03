import http.server
import socketserver

# Define the port for the web server
port = 8080

# Define the content for your webpage
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>DoodleWorld - Drawing Pad for Kids</title>
</head>
<body>
    <h1>Welcome to DoodleWorld</h1>
    <p>DoodleWorld is a fun and creative drawing application designed for children of all ages. It's a great tool for enhancing your child's artistic skills while having loads of fun!</p>
    <h2>Features:</h2>
    <ul>
        <li>Easy-to-use drawing tools</li>
        <li>Colorful and engaging interface</li>
        <li>Educational value for fine motor skills</li>
        <li>Parent-child bonding through creativity</li>
    </ul>
    <h2>Target Audience:</h2>
    <p>DoodleWorld is suitable for children aged 1 to 12, regardless of gender or socioeconomic background.</p>
</body>
</html>
"""

# Create a simple HTTP server
with socketserver.TCPServer(("", port), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Server started on port {port}")
    
    # Serve the HTML content
    httpd.serve_forever()
