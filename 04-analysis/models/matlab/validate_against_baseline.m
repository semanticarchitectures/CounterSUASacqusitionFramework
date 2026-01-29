function [ok, messages] = validate_against_baseline(result, baseline)
%VALIDATE_AGAINST_BASELINE Compare results to baseline expectations.

messages = {};
tolerance = baseline.tolerance;

expected = baseline.expected;
expected_threats = expected.threat_results;

if numel(result.threat_results) ~= numel(expected_threats)
    messages{end+1} = 'Threat count does not match baseline.';
end

for i = 1:numel(expected_threats)
    exp_threat = expected_threats(i);
    match = [];
    for j = 1:numel(result.threat_results)
        if strcmp(result.threat_results(j).id, exp_threat.id)
            match = result.threat_results(j);
            break;
        end
    end
    if isempty(match)
        messages{end+1} = sprintf('Missing threat result: %s', exp_threat.id);
        continue;
    end
    if abs(match.pd_max - exp_threat.pd_max) > tolerance
        messages{end+1} = sprintf('Pd mismatch for %s: got %.3f expected %.3f', ...
            exp_threat.id, match.pd_max, exp_threat.pd_max);
    end
end

summary = expected.summary;
if abs(result.summary.pd_mean - summary.pd_mean) > tolerance
    messages{end+1} = sprintf('pd_mean mismatch: got %.3f expected %.3f', ...
        result.summary.pd_mean, summary.pd_mean);
end
if abs(result.summary.pd_min - summary.pd_min) > tolerance
    messages{end+1} = sprintf('pd_min mismatch: got %.3f expected %.3f', ...
        result.summary.pd_min, summary.pd_min);
end
if abs(result.summary.pd_max - summary.pd_max) > tolerance
    messages{end+1} = sprintf('pd_max mismatch: got %.3f expected %.3f', ...
        result.summary.pd_max, summary.pd_max);
end

ok = isempty(messages);
end

