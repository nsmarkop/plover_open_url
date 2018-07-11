Plover Open URL
===============

Command plugin for
`Plover <https://github.com/openstenoproject/plover>`__ to open a URL, a
folder, or files.

The package is available on
`GitHub <https://github.com/nsmarkop/plover_open_url>`__ and
`PyPI <https://pypi.org/project/plover-open-url/>`__.

Usage
-----

In order to use this plugin in
`Plover <https://github.com/openstenoproject/plover>`__ you need to
create a dictionary entry of the form:

.. code:: json

    {
        "example_stroke": "{PLOVER:OPEN_URL:url}"
    }

For example, if you wanted to open Google:

.. code:: json

    {
        "example_stroke": "{PLOVER:OPEN_URL:https://www.google.com}"
    }

or if you wanted to open Program Files on Windows:

.. code:: json

    {
        "example_stroke": "{PLOVER:OPEN_URL:C:\\Program Files}"
    }

License
-------

The MIT License.
