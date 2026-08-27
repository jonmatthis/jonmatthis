use anyhow::Result;
use chrono::NaiveDate;
use plotly::{
    Configuration, Layout, Plot, Scatter,
    common::{AxisSide, Line},
    layout::{Axis, AxisType},
};
use polars::prelude::*;

fn main() -> Result<()> {
    let csv_path = "startrail-freemocap-freemocap.csv";

    let stars = load_stars(csv_path)?;
    let velocity = compute_velocity(&stars);
    println!("Loaded {} data points", stars.len());

    let dates: Vec<String> = stars
        .iter()
        .map(|p| {
            chrono::DateTime::from_timestamp(p[0] as i64, 0)
                .map(|dt| dt.format("%Y-%m-%d").to_string())
                .unwrap_or_default()
        })
        .collect();
    let star_vals: Vec<f64> = stars.iter().map(|p| p[1]).collect();
    let vel_vals: Vec<f64> = velocity.iter().map(|p| p[1]).collect();

    let red = "rgb(200,60,60)";
    let blue = "rgb(60,120,220)";

    // ── top subplot — linear ────────────────────────────────────────
    let stars_linear = Scatter::new(dates.clone(), star_vals.clone())
        .name("Stars")
        .x_axis("x")
        .y_axis("y")
        .line(Line::new().color(red));

    let vel_linear = Scatter::new(dates.clone(), vel_vals.clone())
        .name("Velocity")
        .x_axis("x")
        .y_axis("y2")
        .line(Line::new().color(blue));

    // ── bottom subplot — log ────────────────────────────────────────
    let stars_log = Scatter::new(dates.clone(), star_vals)
        .name("Stars (log)")
        .x_axis("x2")
        .y_axis("y3")
        .line(Line::new().color(red))
        .show_legend(false);

    let vel_log = Scatter::new(dates, vel_vals)
        .name("Velocity (log)")
        .x_axis("x2")
        .y_axis("y4")
        .line(Line::new().color(blue))
        .show_legend(false);

    // ── layout ──────────────────────────────────────────────────────
    let layout = Layout::new()
        .title("GitHub Stars — freemocap/freemocap")
        // top — linear
        .x_axis(Axis::new().anchor("y"))
        .y_axis(Axis::new().title("Stars").side(AxisSide::Left).domain(&[0.55, 1.0]))
        .y_axis2(
            Axis::new()
                .title("Velocity (stars/day)")
                .side(AxisSide::Right)
                .domain(&[0.55, 1.0])
                .overlaying("y"),
        )
        // bottom — log
        .x_axis2(Axis::new().anchor("y3").matches("x"))
        .y_axis3(
            Axis::new()
                .title("Stars (log)")
                .side(AxisSide::Left)
                .domain(&[0.0, 0.45])
                .type_(AxisType::Log),
        )
        .y_axis4(
            Axis::new()
                .title("Velocity (log)")
                .side(AxisSide::Right)
                .domain(&[0.0, 0.45])
                .type_(AxisType::Log)
                .overlaying("y3"),
        );

    let mut plot = Plot::new();
    plot.add_trace(stars_linear);
    plot.add_trace(vel_linear);
    plot.add_trace(stars_log);
    plot.add_trace(vel_log);
    plot.set_layout(layout);
    plot.set_configuration(Configuration::new().responsive(true));
    plot.write_html("stars.html");

    println!("Wrote stars.html");

    let _ = std::process::Command::new("cmd")
        .args(["/c", "start", "stars.html"])
        .spawn();

    Ok(())
}

fn parse_date(s: &str) -> Option<f64> {
    let d = NaiveDate::parse_from_str(s, "%Y-%m-%d").ok()?;
    Some(d.and_hms_opt(0, 0, 0)?.and_utc().timestamp() as f64)
}

fn load_stars(path: &str) -> Result<Vec<[f64; 2]>> {
    let df = LazyCsvReader::new(path.into())
        .with_has_header(true)
        .finish()?
        .collect()?;

    let dates = df.column("Date")?.str()?;
    let stars_col = df.column("freemocap/freemocap")?.i64()?;

    Ok(dates
        .into_iter()
        .zip(stars_col.into_iter())
        .filter_map(|(d, s)| Some([parse_date(d?)?, s? as f64]))
        .collect())
}

fn compute_velocity(stars: &[[f64; 2]]) -> Vec<[f64; 2]> {
    let mut v = Vec::with_capacity(stars.len());
    for i in 0..stars.len() {
        let dv = if i == 0 { 0.0 } else { stars[i][1] - stars[i - 1][1] };
        v.push([stars[i][0], dv]);
    }
    v
}
