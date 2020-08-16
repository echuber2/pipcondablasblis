# pipcondablasblis
A hack to change blas build to blis, but as a pip requirement

## What it does

When installed with `pip`, it invokes this at install time:

```bash
conda install -y blas=*=blis
```

That's all it does. Pip hides the output that conda generates while this happens so it will take a while without showing any output.

