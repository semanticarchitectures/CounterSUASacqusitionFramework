function baseline = load_baseline(baselinePath)
%LOAD_BASELINE Load baseline JSON into a MATLAB struct.

raw = fileread(baselinePath);
baseline = jsondecode(raw);
end

