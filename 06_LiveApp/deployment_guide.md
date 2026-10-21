# 🌐 線上 Live Demo 訪問與部署指南

## 一、一鍵 Docker 容器部署
```bash
docker build -t phantom-grid-202612_kiroween_dark_mode_hackathon .
docker run -d -p 8080:8080 phantom-grid-202612_kiroween_dark_mode_hackathon
```

## 二、雲端預覽端點
- **Interactive Web UI**: `http://localhost:8080`
- **CLI TUI Live Stream**: `python -m cli.tui_live_stream`
