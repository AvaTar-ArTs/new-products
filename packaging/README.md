# Release builder

Build a reviewable metadata bundle from an explicit package manifest:

```bash
python packaging/build_release.py workvault-control \
  --output dist/workvault-control-0.1.0.zip
```

The builder does not recursively package `/Users/steven`, `/Volumes`, model
directories, caches, or credentials. Add only reviewed files through a
manifest's optional `package_files` allow-list. A ZIP is not automatically a
Setapp artifact: native app packaging, signing, notarization, clean-machine
testing, and channel approval remain separate release gates.
