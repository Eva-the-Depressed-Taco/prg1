import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Plum
		self._button1.Location = System.Drawing.Point(91, 115)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "show name"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(129, 18)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(129, 45)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 2
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightPink
		self._label1.Location = System.Drawing.Point(21, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(91, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "first name"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightPink
		self._label2.Location = System.Drawing.Point(21, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(91, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "last name"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightPink
		self._label3.Location = System.Drawing.Point(19, 78)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(91, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "full name"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightPink
		self._label4.Location = System.Drawing.Point(116, 78)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(140, 23)
		self._label4.TabIndex = 6
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(64, 0, 64)
		self.ClientSize = System.Drawing.Size(284, 139)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "names"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		fn = self._textBox1.Text
		ln = self._textBox2.Text
		self._label4.Text = str(fn) + " " + str(ln)