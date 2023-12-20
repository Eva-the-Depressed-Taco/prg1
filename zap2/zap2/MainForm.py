import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Pink
		self._label1.Location = System.Drawing.Point(135, 110)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Pink
		self._label10.Location = System.Drawing.Point(12, 110)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 5
		self._label10.Text = "price"
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Pink
		self._label3.Location = System.Drawing.Point(135, 192)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Pink
		self._label8.Location = System.Drawing.Point(12, 192)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 7
		self._label8.Text = "city tax"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Pink
		self._label4.Location = System.Drawing.Point(135, 150)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 3
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Pink
		self._label7.Location = System.Drawing.Point(12, 150)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 8
		self._label7.Text = "surchage"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(135, 50)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Plum
		self._button1.Location = System.Drawing.Point(12, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "calcualte"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Pink
		self._label11.Location = System.Drawing.Point(12, 47)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 10
		self._label11.Text = "killowatts used"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(266, 297)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label8)
		self.Name = "MainForm"
		self.Text = "zap2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		zaps = int(self._textBox1.Text)
		bill = zaps * 0.0475
		cityt = bill * 0.03
		scharge = bill * 0.10
		total = bill + cityt + scharge
		latef = total *1.04
		self._label1.Text = str(bill)(latef,2)
		self._label4.Text = str(scharge)(latef,2)
		self._label3.Text = str(cityt)(latef,2)
		self._label2.Text = str(total)(latef,2)
		self._label5.Text = str(round(latef,2)