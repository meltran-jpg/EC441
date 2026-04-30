# Wireshark HTTP + TCP Analysis

## Objective
Observe real network traffic to understand:
- HTTP request/response
- TCP 3-way handshake

## Steps
1. Open Wireshark
2. Filter: `http || tcp`
3. Visit http://example.com
4. Stop capture

## Observations

### TCP Handshake
- SYN → client initiates connection
- SYN-ACK → server responds
- ACK → connection established

### HTTP Request
GET / HTTP/1.1

### HTTP Response
HTTP/1.1 200 OK

## Key Insight
This shows how application-layer protocols (HTTP) rely on transport-layer reliability (TCP).

## Artifact
Screenshot saved as capture.png
