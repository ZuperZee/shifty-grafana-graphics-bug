# Shifty grafana graphics bug

A small example repo for testing the bug <https://github.com/grafana/grafana/issues/82214>

dashboard.json contains a Grafana dashboard using the dash.svg file.

You might have to scale the svg in the panel to see the bug.

## Serving svg

To serve the dash.svg file run

```py
python3 serve.py
```
