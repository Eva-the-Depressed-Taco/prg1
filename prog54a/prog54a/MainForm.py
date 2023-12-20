import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._comboBox1 = System.Windows.Forms.ComboBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# comboBox1
		# 
		self._comboBox1.FormattingEnabled = True
		self._comboBox1.Items.AddRange(System.Array[System.Object](
			["1970 VW Bug",
			"1979 Firebird",
			"1980 Subaru",
			"1975 Cutlass"]))
		self._comboBox1.Location = System.Drawing.Point(184, 33)
		self._comboBox1.Name = "comboBox1"
		self._comboBox1.Size = System.Drawing.Size(121, 21)
		self._comboBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(122, 33)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(56, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "car select"
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleVioletRed
		self._button1.Location = System.Drawing.Point(59, 193)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleVioletRed
		self._button2.Location = System.Drawing.Point(59, 222)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleVioletRed
		self._button3.Location = System.Drawing.Point(59, 251)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(122, 72)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(56, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "miles"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(122, 147)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(265, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "miles per gallan"
		# 
		# label4
		# 
		self._label4.Location = System.Drawing.Point(122, 109)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(56, 23)
		self._label4.TabIndex = 7
		self._label4.Text = "gallons"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Thistle
		self._label5.Location = System.Drawing.Point(249, 109)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(56, 23)
		self._label5.TabIndex = 10
		self._label5.Text = " "
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Thistle
		self._label6.Location = System.Drawing.Point(249, 147)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(56, 23)
		self._label6.TabIndex = 9
		self._label6.Text = " "
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Thistle
		self._label7.Location = System.Drawing.Point(249, 72)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(56, 23)
		self._label7.TabIndex = 8
		self._label7.Text = " "
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Orchid
		self.ClientSize = System.Drawing.Size(907, 438)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._comboBox1)
		self.Name = "MainForm"
		self.Text = "prog54a"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		miles = 0
		gallons = 0
		mpg = 0
		car = self._comboBox1.Text
		
		if car == "1970 VW Bug":			
			miles = 286
			gallons = 9
		if car == "1979 Firebird":
			miles = 412
			gallons = 40
		if car == "1980 Subaru":
			miles = 361
			gallons = 18
		if car == "1975 Cutlass":
			miles = 161
			gallons = 11
		mpg = float(miles) / float(gallons)
		mpg = round(mpg, 10)
		
		
		
		self._label6.Text = str(mpg)

	def Button2Click(self, sender, e):
		self._Application.Exit

	def Button3Click(self, sender, e):
		self._label6.Text = ""