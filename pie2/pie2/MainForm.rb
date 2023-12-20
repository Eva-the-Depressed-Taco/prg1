require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(92, 116)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 0
		@button1.Text = "button1"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(92, 165)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 1
		@button2.Text = "button2"
		@button2.UseVisualStyleBackColor = true
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(92, 210)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(75, 23)
		@button3.TabIndex = 2
		@button3.Text = "button3"
		@button3.UseVisualStyleBackColor = true
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(92, 63)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(100, 20)
		@textBox1.TabIndex = 3
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Orchid
		@label1.Location = System::Drawing::Point.new(205, 156)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 4
		@label1.Text = "label1"
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.Orchid
		@label2.Location = System::Drawing::Point.new(311, 156)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(100, 23)
		@label2.TabIndex = 5
		@label2.Text = "label2"
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.FromArgb(255, 192, 192)
		self.ClientSize = System::Drawing::Size.new(573, 414)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "pie2"
		self.ResumeLayout(false)
		self.PerformLayout()
	end
	def Button1Click(sender, e)
		radius = str(Self.textBox1.Text)
		pie = 3.141592653589793238462643383279502884197
		area = (radius**2) * pie
		circ = radius * pie
		Self._.Text = str(area)
		Self._label2.Text = str(circ)
	end
end

