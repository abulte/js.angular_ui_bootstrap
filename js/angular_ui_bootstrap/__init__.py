from fanstatic import Library, Resource, Group
from js.angular import angular

library = Library('angularuibootstrap', 'resources')

angular_ui_bootstrap = Resource(
    library, 'ui-bootstrap-tpls-0.11.0.js',
    minified='ui-bootstrap-tpls-0.11.0.min.js',
    depends=[angular])