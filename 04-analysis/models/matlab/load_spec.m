function spec = load_spec(specPath)
%LOAD_SPEC Load a scenario spec JSON into a MATLAB struct.

raw = fileread(specPath);
spec = jsondecode(raw);
end



