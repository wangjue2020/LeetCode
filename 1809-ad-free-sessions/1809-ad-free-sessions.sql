# Write your MySQL query statement below
select session_id from playback left join ads on ads.timestamp >= start_time and timestamp <= end_time and ads.customer_id = playback.customer_id where ad_id is null;