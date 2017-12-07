from jinja2 import Environment, FileSystemLoader


def save_to_html(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as html_page:
        html_page.write(content)


def render_index_html(template, title, static_path):
    return template.render(
                    title=title,
                    static_path=static_path)


def render_orders_html(template, title, static_path):
    return template.render(
                    title=title, 
                    static_path=static_path)


if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader(searchpath='templates'))

    # INDEX PAGE RENDERING
    index_template = env.get_template('index_template.html')

    index_content_to_save = render_index_html(
                                    index_template,
                                    'Главная страница',
                                    'static')

    save_to_html('docs/index_generated.html', index_content_to_save)

    # ORDERS PAGE RENDERING
    orders_template = env.get_template('orders_template.html')

    orders_content_to_save = render_orders_html(
                                    orders_template,
                                    'Личный кабинет',
                                    'static')

    save_to_html('docs/orders_generated.html', orders_content_to_save)
