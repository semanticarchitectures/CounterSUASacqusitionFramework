function run_scenario(specPath, outPath)
%RUN_SCENARIO Load a scenario spec and execute the model.
%   run_scenario(specPath, outPath) writes JSON output to outPath.

if nargin < 1 || isempty(specPath)
    error('specPath is required.');
end

spec = load_spec(specPath);
result = simulate_scenario(spec);

if nargin >= 2 && ~isempty(outPath)
    fid = fopen(outPath, 'w');
    if fid < 0
        error('Unable to open output path: %s', outPath);
    end
    fwrite(fid, jsonencode(result, 'PrettyPrint', true));
    fclose(fid);
else
    disp(jsonencode(result, 'PrettyPrint', true));
end
end



