================================
Considerations for binary wheels
================================

Python packages with native code have a set of unique challenges not present
in pure packages. The more complex the native code, the more complex the
packaging can become. Issues arrise around topics such as non-Python compiled
dependencies ("native dependencies"), the importance of the ABI (Application
Binary Interface) of native code, dependency on SIMD code and cross
compilation. In depth discussion of these and many more topics and issues around
 native packaging is available at
 `pypackaging-native<https://pypackaging-native.github.io/>`_.
