import pandas as pd
import streamlit as st
import plotly.express as px


def setup_pandas_display():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.width', 1000)

def load_data():
    df = pd.read_csv("50krecords.csv")
    return df

def feature_engineering(df):

    df['hour'] = pd.to_datetime(df['hour'])

    df['year'] = df['hour'].dt.year
    df['month'] = df['hour'].dt.month
    df['day'] = df['hour'].dt.day
    df['weekday'] = df['hour'].dt.day_name()
    df['hour_of_day'] = df['hour'].dt.hour

    # Drop unnecessary columns
    df.drop(columns=['id','site_id','app_id','device_id','device_ip'], axis=1, inplace=True)
    return df


def calculate_kpis(df):
    total_impressions = len(df)
    total_clicks = df['click'].sum()
    ctr = total_clicks / total_impressions * 100 if total_impressions > 0 else 0
    return total_impressions, total_clicks, ctr


def top10_chart(df, col_name, color_scale):
    temp = df.groupby(col_name)['click'].agg(['sum','count']).reset_index()
    temp['ctr'] = temp['sum'] / temp['count'] * 100
    top10 = temp.sort_values('ctr', ascending=False).head(10)

    fig = px.bar(
        top10,
        x=col_name,
        y='ctr',
        text='ctr',
        color='ctr',
        color_continuous_scale=color_scale,
        title=f"Top 10 CTR by {col_name}"
    )
    fig.update_traces(
        texttemplate='%{text:.2f}%',
        hovertemplate=f"{col_name}: %{{x}}<br>CTR: %{{y:.2f}}%"
    )
    return fig


def run_dashboard(df):
    st.title("Avazu CTR Marketing Dashboard")
    st.markdown("This dashboard provides insights into click-through rate performance across devices, apps, and sites.")


    st.sidebar.header("Filters")


    min_date, max_date = df['hour'].dt.day.min(), df['hour'].dt.day.max()
    available_days = df['hour'].dt.day.unique()

    if len(available_days) > 1:
        date_range = st.sidebar.slider(
            "Select Date Range",
            min_value=min_date,
            max_value=max_date,
            value=(min_date, max_date)
        )

        filtered_df = df[
            (df['hour'].dt.day >= date_range[0]) &
            (df['hour'].dt.day <= date_range[1])
            ]
    else:
        st.sidebar.warning(f"⚠ Only one day available: {available_days[0]}. Showing all records.")
        filtered_df = df.copy()


    device_filter = st.sidebar.multiselect(
        "Device Type",
        options=filtered_df['device_type'].unique(),
        default=None
    )
    if device_filter:
        filtered_df = filtered_df[filtered_df['device_type'].isin(device_filter)]


    app_filter = st.sidebar.multiselect(
        "App Category",
        options=filtered_df['app_category'].unique(),
        default=None
    )
    if app_filter:
        filtered_df = filtered_df[filtered_df['app_category'].isin(app_filter)]


    site_filter = st.sidebar.multiselect(
        "Site Category",
        options=filtered_df['site_category'].unique(),
        default=None
    )
    if site_filter:
        filtered_df = filtered_df[filtered_df['site_category'].isin(site_filter)]


    st.markdown("## Key Metrics")
    col1, col2, col3 = st.columns(3)
    total_impressions, total_clicks, ctr = calculate_kpis(filtered_df)
    col1.metric("Total Impressions", f"{total_impressions:,}")
    col2.metric("Total Clicks", f"{total_clicks:,}")
    col3.metric("Overall CTR", f"{ctr:.2f}%")


    st.markdown("## CTR Analysis")
    st.plotly_chart(top10_chart(filtered_df, 'app_category', 'Blues'), use_container_width=True)
    st.plotly_chart(top10_chart(filtered_df, 'site_category', 'Greens'), use_container_width=True)
    st.plotly_chart(top10_chart(filtered_df, 'device_model', 'Oranges'), use_container_width=True)
    st.plotly_chart(top10_chart(filtered_df, 'device_type', 'Purples'), use_container_width=True)


    st.markdown("## CTR Over Time")
    time_series = filtered_df.groupby(filtered_df['hour'].dt.date)['click'].agg(['sum','count']).reset_index()
    time_series['ctr'] = time_series['sum'] / time_series['count'] * 100
    time_series.rename(columns={'hour': 'date'}, inplace=True)

    fig_time = px.line(
        time_series,
        x='date',
        y='ctr',
        title="Daily CTR Trend",
        markers=True
    )
    st.plotly_chart(fig_time, use_container_width=True)


if __name__ == '__main__':
    setup_pandas_display()
    data = load_data()
    data = feature_engineering(data)
    run_dashboard(data)
