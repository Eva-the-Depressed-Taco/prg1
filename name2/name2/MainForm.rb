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
		@label1 = System::Windows::Forms::Label.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(157, 129)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 0
		@button1.Text = "button1"
		@button1.UseVisualStyleBackColor = true
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(166, 159)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 1
		@button2.Text = "button2"
		@button2.UseVisualStyleBackColor = true
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.DarkSlateBlue
		@label1.ForeColor = System::Drawing::Color.Orchid
		@label1.Location = System::Drawing::Point.new(305, 128)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(100, 23)
		@label1.TabIndex = 2
		@label1.Text = "label1"
		# 
		# MainForm
		# 
		self.BackColor = System::Drawing::Color.MediumPurple
		self.ClientSize = System::Drawing::Size.new(611, 423)
		self.Controls.Add(@label1)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "name2"
		self.ResumeLayout(false)
	end
end

