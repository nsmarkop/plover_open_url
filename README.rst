Plover Open URL
===============

Command plugin for
`Plover <https://github.com/openstenoproject/plover>`__ to open a URL.

Installation
------------

Download the latest version of Plover for your operating system from the
`releases page <https://github.com/openstenoproject/plover/releases>`__.
Only versions 4.0.0.dev6 and higher are supported.

1. Open Plover
2. Navigate to the Plugin Manager tool
3. Select the “plover-open-url” plugin entry in the list
4. Click install
5. Restart Plover

The same method can be used for updating and uninstalling the plugin.

Usage
-----

In order to use this plugin you just need to create a dictionary entry
of the form:

.. code:: json

    {
        "example_stroke": "{PLOVER:OPEN_URL:url}"
    }

For example, if you wanted to open Google:

.. code:: json

    {
        "example_stroke": "{PLOVER:OPEN_URL:https://www.google.com}"
    }
