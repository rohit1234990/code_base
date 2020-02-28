from flask import Blueprint, request, jsonify
from db_helper import connect, insert, select_one, select_all, delete_helper, edit_helper
import jwt


post = Blueprint('post', __name__)

# write routes here
@post.route('/create', methods=['POST'])
def create():
    category_id = request.json['category_id']
    heading     = request.json['heading']
    body        = request.json['body']
    token       = request.json['token']
    user_id     = request.json['user_id']

    try:
        decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
        user_id = decoded['user_id']
    except Exception:
        return jsonify({'result':'failure', 'user': 'invalid'})

    query = '''INSERT INTO `blog` (`category_id`, `user_id`, `heading`, `body`, `created_on`)
               VALUES (%s, %s, %s, %s, CURDATE())
            '''
    arguments = [category_id, user_id, heading, body]
    result = insert(query, arguments)
    return jsonify(result)

@post.route('/category')
def get_all_category():
    query = 'SELECT * FROM `category` ORDER BY `category` ASC'
    result = select_all(query, [])
    return jsonify(result)

@post.route('/blogs', methods=['GET', 'POST'])
def get_all_blogs():
    if request.method == 'GET':
        # query = 'SELECT * FROM `blog`'
        query = '''SELECT blog.`blog_id`, blog.`heading`, blog.`body`, user.`name` FROM `blog` 
                    LEFT JOIN `user` ON blog.`user_id` = user.`user_id`
                '''
        result = select_all(query, [])
        return jsonify(result)
    elif request.method == 'POST':
        n = int(request.json['n'])
        query = "SELECT * FROM `blog` ORDER BY `created_on` LIMIT %s"
        result = select_all(query, [n])
        return jsonify(result)


@post.route('/blogs/<int:blog_id>')
def get_blog_by_id(blog_id):
    query = 'SELECT * FROM `blog` WHERE `blog_id` = %s'
    result = select_one(query, [blog_id])
    return jsonify(result)

@post.route('/blogs/user/<int:user_id>')
def get_blog_by_user_id(user_id):
    query = 'SELECT * FROM `blog` WHERE `user_id` = %s'
    result = select_all(query, [user_id])
    return jsonify(result)



@post.route('/comments', methods=['POST'])
def post_comment():
    blog_id = request.json['blog_id']
    comment = request.json['comment']
    user_id = request.json['user_id']

    query = '''INSERT INTO `comment` (blog_id, user_id, commented_on, comment)
               VALUES (%s, %s, CURDATE(), %s)
            '''
    arguments = [blog_id, user_id, comment]
    result = insert(query, arguments)
    return jsonify(result)



@post.route('/comments/<int:blog_id>')
def get_comments_by_blog_id(blog_id):
    # query = 'SELECT `comment` FROM `comment` WHERE `blog_id` = %s'
    query = """SELECT comment.comment, user.name FROM comment 
               LEFT JOIN user ON comment.user_id = user.user_id WHERE comment.`blog_id` = %s
            """
    result = select_all(query, [blog_id])
    return jsonify(result)



@post.route('/delete/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    try:
        token = request.json['token']
        user_id = request.json['user_id']

        # decode the token
        decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
        if int(decoded['user_id']) != int(user_id):
            return jsonify({'result':'failure', 'error': 'authentication failed' })
        
        query_arr = []
        # first we have to delete associated comments
        query_arr.append(['DELETE FROM `comment` WHERE `blog_id` = %s', [blog_id]])
        # later delete the blog
        query_arr.append(['DELETE FROM `blog` WHERE `blog_id` = %s', [blog_id]])
        
        result = delete_helper(query_arr)
        return jsonify(result)
    except Exception:
        return jsonify({'result':'failure', 'error': 'some error occured' })

    

@post.route('/edit/<int:blog_id>', methods=['PUT'])
def edit(blog_id):
    try:
        heading = request.json['heading']
        body    = request.json['body']
        token   = request.json['token']
        user_id = request.json['user_id']

        # decode the token
        decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
        if int(decoded['user_id']) != int(user_id):
            return jsonify({'result':'failure', 'error': 'authentication failed' })

        query = '''UPDATE `blog` SET 
                `heading` = %s,
                `body`    = %s
                    WHERE `blog_id` = %s
                '''
        result = edit_helper(query, [heading, body, blog_id])
        return jsonify(result)
    except Exception as ex:
            return jsonify({'result':'failure', 'error': ex })

    

