def validate(): username = Element("username").value password = Element("password").value result = Element("result") 
Username validation if len(username) < 7: result.write("❌ Username must be at least 7 characters long.") return 
Password validation if len(password) < 10: result.write("❌ Password must be at least 10 characters long.") return if not any
(c.isalpha() for c in password): result.write("❌ Password must contain at least one letter.") return if not any(c.isdigit() for c in password): result.write("❌ Password must contain at least one number.") return  # pyright: ignore[reportInvalidTypeForm]
result.write("✅ Account created successful")