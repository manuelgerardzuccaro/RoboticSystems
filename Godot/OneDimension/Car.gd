extends RigidBody2D
@onready var slider_label = $"../InputForce"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	print("P = ", self.global_position.x, ", V = ", self.linear_velocity.x)

var force = 1000


func _integrate_forces(state):
	if Input.is_action_pressed("ui_right"):
		state.apply_central_force(Vector2(force,0))
	elif Input.is_action_pressed("ui_left"):
		state.apply_central_force(Vector2(-force,0))


func _on_v_slider_value_changed(value):
	slider_label.text = str(value) + " Kg px/s^2"
	force = value
