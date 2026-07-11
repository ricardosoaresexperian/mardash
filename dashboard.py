import marimo

__generated_with = "0.23.13"
app = marimo.App(width="full")

@app.cell
def _():
    import altair as alt
    import marimo as mo
    import pandas as pd

    return alt, mo, pd


@app.cell
def _(pd):
    data = pd.DataFrame(
        {"category": ["A", "B", "C", "D"], "value": [25, 45, 15, 30]}
    )
    return (data,)


@app.cell
def _(alt, data):
    chart = (
        alt.Chart(data)
        .mark_bar()
        .encode(
            x="category:N",
            y="value:Q",
        )
        .properties(width=600, height=400)
    )
    return (chart,)


@app.cell
def _(chart, mo):
    interactive_chart = mo.ui.altair_chart(chart)
    interactive_chart
    return


if __name__ == "__main__":
    app.run()
