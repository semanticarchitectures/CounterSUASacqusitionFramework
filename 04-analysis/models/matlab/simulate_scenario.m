function result = simulate_scenario(spec)
%SIMULATE_SCENARIO Execute a simple multi-sensor Pd model.

threats = spec.threats;
sensors = spec.sensors;

threat_results = repmat(struct('id', '', 'pd_max', 0), numel(threats), 1);
pd_values = zeros(numel(threats), 1);

for i = 1:numel(threats)
    threat = threats(i);
    pd_max = 0;
    for j = 1:numel(sensors)
        sensor = sensors(j);
        pd = compute_pd(sensor, threat);
        if pd > pd_max
            pd_max = pd;
        end
    end
    threat_results(i).id = threat.id;
    threat_results(i).pd_max = round(pd_max, 3);
    pd_values(i) = pd_max;
end

result = struct();
result.scenario_id = spec.scenario_id;
result.threat_results = threat_results;
result.summary = struct();
result.summary.pd_mean = round(mean(pd_values), 3);
result.summary.pd_min = round(min(pd_values), 3);
result.summary.pd_max = round(max(pd_values), 3);
result.policy = spec.policy;
end



