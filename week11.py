# PART 1
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
# PART 2
to_do_items = [{'title': 'Item 1', 'description': 'Description of item 1'},
               {'title': 'Item 2', 'description': 'Description of item 2'},
               {'title': 'Item 3', 'description': 'Description of item 3'},
<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Description</th>
    </tr>
  </ { % < thead >
     < tbody
for item in to_do_items %}
    <tr>
      <td>{{ item.title }}</td>
      <td>{{ item.description }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
from flask import render_template

@app.route('/')
def show_to_do_list():
    return render_template('to_do_list.html', to_do_items=to_do_item


#Part 3
<form action="/submit-todo-item" method="post">
  <label for="task">Task:</label>
  <input type="text" name="task" id="task">
  <br>
  <label for="email">Email:</label>
  <input type="email" name="email" id="email">
  <br>
  <label for="priority">Priority:</label>
  <select name="priority" id="priority">
    <option value="low">Low</option>
    <option value="medium">Medium</option>
    <option value="high">High</option>
  </select>
  <br>
  <input type="submit" value="Add To Do Item">
</form>