**Package Release**
===================

This is the reference guide for manimce. The package post manimce
0.1.1.post0 was posted today and inform you that the package will be
deprecated going forward.

Further work on manimce has been integrated into manim. Originally, this
project was meant to be in the manim package. However, the name manim
was not available by the PyPA support because some malware was uploaded
with the name at the time. To avoid delays in subsequent releases, the
package name manimce was used for updates. The issue with manim was
later fixed by PyPA, unblocking the package name for usage. Upon this
development, manimce was no longer needed. All updates and releases
moved to manim.

Thus, if you wish to work on the most updated package with support from
our team, refer to the manim package. Make sure to uninstall the manimce
package from your virtual environment before installing or updating
manim. This is to avoid any conflict during installation.

To do this, run the following command in your virtual environment.

pip uninstall -y manimce && pip install manim

If for some reason, you decide to go ahead with the manimce package, you
will get a DeprecationWarning upon installing the module if you have set
your development environment with –W error and your pytest configs with
filewarnings = error. You could simply ignore this warning.
