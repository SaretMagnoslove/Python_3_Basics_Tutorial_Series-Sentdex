import sqlite3

# First, let's run an update. Before that, we'll look at the existing data:
def del_and_update():
    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data
    # Now, we can update some data, like:
    c.execute('UPDATE stuffToPlot SET value = 99 WHERE value = 3')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]
    # Finally, we can delete things:
    c.execute('DELETE FROM stuffToPlot WHERE value = 99')
    conn.commit()

    c.execute('SELECT * FROM stuffToPlot')
    data = c.fetchall()
    [print(row) for row in data]