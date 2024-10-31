# notifications

## Deploy on container

```bash
podman pull ghcr.io/grisha765/notifications:latest
podman run --tmpfs /tmp \
--name notifications \
--network="host" \
-e CAMERA_TOPIC="ergolyam" \
-e NTFY_SERV="https://ntfy.sh/" \
ghcr.io/grisha765/notifications:latest
```
