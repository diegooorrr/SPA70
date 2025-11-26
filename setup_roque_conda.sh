#!/usr/bin/env bash
set -e
export PATH="$HOME/miniforge3/bin:$PATH"
conda --version
ENV=roque
if conda env list | awk '{print $1}' | grep -xq "$ENV"; then
  echo "Conda env '$ENV' already exists - skipping create"
else
  echo "Creating conda env '$ENV' with python=3.11 and streamlit (from conda-forge)..."
  conda create -y -n "$ENV" python=3.11 -c conda-forge streamlit
fi

echo "Verifying streamlit in env '$ENV'..."
conda run -n "$ENV" streamlit --version || true

LOGFILE=roque_streamlit.log
PIDFILE=roque_streamlit.pid
if [ -f "$PIDFILE" ]; then
  if kill -0 "$(cat $PIDFILE)" >/dev/null 2>&1; then
    echo "Streamlit already appears to be running (pid $(cat $PIDFILE)). Logs: $LOGFILE"
    exit 0
  else
    echo "Removing stale pidfile"
    rm -f "$PIDFILE"
  fi
fi

echo "Starting Streamlit in conda env '$ENV' (logs -> $LOGFILE)"
conda run -n "$ENV" streamlit run roadmap.py --server.port 8501 --server.headless true &> "$LOGFILE" &
echo $! > "$PIDFILE"

sleep 1

echo "--- log tail ---"
tail -n 40 "$LOGFILE" || echo "(log file not created yet)"
