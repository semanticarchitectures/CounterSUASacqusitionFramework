function run_parity_tests
%RUN_PARITY_TESTS Execute baseline parity checks for MATLAB model.

root = fullfile(fileparts(mfilename('fullpath')), '..');
cases = {
    struct('spec', 'sample-scenario.json', 'baseline', 'sample-baseline.json'), ...
    struct('spec', 'convoy-scenario.json', 'baseline', 'convoy-baseline.json') ...
};

for i = 1:numel(cases)
    specPath = fullfile(root, 'specs', cases{i}.spec);
    baselinePath = fullfile(root, 'baselines', cases{i}.baseline);

    spec = load_spec(specPath);
    result = simulate_scenario(spec);
    baseline = load_baseline(baselinePath);

    [ok, messages] = validate_against_baseline(result, baseline);
    if ~ok
        error(strjoin(messages, newline));
    end
end

disp('Parity tests passed.');
end

