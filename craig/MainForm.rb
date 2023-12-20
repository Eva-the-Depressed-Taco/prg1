require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		resources = System::Resources::ResourceManager.new("craig.MainForm", System::Reflection::Assembly.GetEntryAssembly())
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.MenuHighlight
		@label1.Location = System::Drawing::Point.new(368, 37)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(468, 137)
		@label1.TabIndex = 0
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button1.Location = System::Drawing::Point.new(299, 278)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(75, 23)
		@button1.TabIndex = 1
		@button1.Text = "show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.ActiveCaption
		@button2.Location = System::Drawing::Point.new(503, 216)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(75, 23)
		@button2.TabIndex = 2
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# MainForm
		# 
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System::Drawing::Size.new(1080, 455)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label1)
		self.Name = "MainForm"
		self.Text = "craig"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "go craig?"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

