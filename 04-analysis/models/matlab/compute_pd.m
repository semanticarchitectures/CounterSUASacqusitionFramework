function pd = compute_pd(sensor, obs)
%COMPUTE_PD Generic probability of detection model.

range_factor = max(0, 1 - obs.range_km / sensor.max_range_km);
orientation_factor = max(0, cosd(obs.orientation_deg));
velocity_factor = min(1, obs.relative_velocity_mps / sensor.ref_velocity_mps);
clutter_factor = max(0, 1 - obs.clutter_index);

pd = sensor.base_pd * range_factor * orientation_factor * ...
    velocity_factor * clutter_factor;
pd = min(1, max(0, pd));
end



