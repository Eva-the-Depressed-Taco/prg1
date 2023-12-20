import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Plum
		self._label2.Location = System.Drawing.Point(374, 108)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Plum
		self._label1.Location = System.Drawing.Point(374, 149)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Violet
		self._button1.Location = System.Drawing.Point(13, 240)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 3
		self._button1.Text = "math"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(52, 91)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 4
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Violet
		self._button2.Location = System.Drawing.Point(12, 335)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 5
		self._button2.Text = "off"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Violet
		self._button3.Location = System.Drawing.Point(12, 285)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 6
		self._button3.Text = "clear"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(949, 441)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label2)
		self.Name = "MainForm"
		self.Text = "thefinalpie"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		radius = int(self._textBox1.Text)
		pie = 3.141592653589793238462643383279502884197
		area = (radius**2) * pie
		circ = radius * pie
		self._label1.Text = str(round(area,3))
		self._label2.Text = str(round(circ,3))

	def Button3Click(self, sender, e):
		self._label2.Text = ""
		self._label1.Text = ""
		self._textBox1.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()