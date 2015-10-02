import MySQLdb


class GatewayMySQL(object):
    def salvar_notas(self, notas):
        connect = MySQLdb.connect(user='root', db='connect')
        cursor = connect.cursor()
        cursor.execute("truncate table notas")
        for nota in notas:
            cursor.execute("insert into notas (nota) values (%s)", nota)
        connect.commit()

    def obter_notas(self):
        connect = MySQLdb.connect(user='root', db='connect')
        cursor = connect.cursor()
        cursor.execute("select nota from notas")
        notas = []
        for nota in cursor:
            notas.append(nota[0])
        return notas
