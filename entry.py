from tianyancha import Tianyancha

if __name__ == '__main__':
    table_dict = Tianyancha(
        username='18600151226',
        password='caonima123',
    ).tianyancha_scraper(
        keyword='北京人人车旧机动车经纪有限公司',
        table='baseInfo',
        export='json',
    )
    print(table_dict)
