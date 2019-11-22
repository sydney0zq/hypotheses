import os
import os.path as osp

TEMPLATE_PREFIX = "templates"

RENDER_CONFIG = {
    'metamds': ['README.md', '404.md', 'src/wishlist.md', 'src/biography.md'],
    'postdir': 'posts',
    'indexfn': 'index.html'
}

TEMPLATE_CONFIG = {
    'meta': osp.join(TEMPLATE_PREFIX, "meta.html"),
    'index': osp.join(TEMPLATE_PREFIX, "index.html"),
    'post': osp.join(TEMPLATE_PREFIX, "post.html"),
    'post-item': osp.join(TEMPLATE_PREFIX, "post-item.html"),
}










