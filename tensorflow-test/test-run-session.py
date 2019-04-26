import tensorflow as tf

state = tf.Variable(0, name="counter")
one = tf.constant(2)

a1 = tf.add(state, one)
a2 = tf.add(state, one)
u1 = tf.assign(state, a1)
u2 = tf.assign(state, a2)

init_op = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init_op) # must be run before other op called
h, g = sess.run([u1, u2]) # u1 u2 are parallel, u1 will not disturb u2, even they share one variable
print(h, g)

sess.close()
