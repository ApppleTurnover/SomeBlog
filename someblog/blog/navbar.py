from someblog.blog import nav

nav.Bar('top', [
    nav.Item('Home', 'index'),
    nav.Item('Blog', 'blog'),
])


# Может еще верну, но на данный момент это не нужно
# from flask_nav import Nav
# from flask_nav.elements import Navbar, View, Text
# from flask_bootstrap.nav import BootstrapRenderer
#
#
# class UserGreeting:
#     def __init__(self):
#         pass
#
#     @property
#     def text(self):
#         return 'Hello, {}'.format('bob')
#
#
# nav = Nav()
#
#
# @nav.navigation()
# def navbar():
#     return Navbar(
#         'MySite',
#         View('Home', 'index'),
#         View('Blog', 'blog'),
#         Text('Lol'),
#         UserGreeting(),
#     )
#
#
# class DarkRenderer(BootstrapRenderer):
#     def visit_Navbar(self, node):
#         nav_tag = super(DarkRenderer, self).visit_Navbar(node)
#         nav_tag['class'] += 'navbar navbar-inverse'  # navbar-fixed-top'
#         return nav_tag
