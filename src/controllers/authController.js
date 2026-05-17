/* Controlador de autenticação de usuários*/

exports.login = async (req, res) => {
  const { email, senha } = req.body;

  if (!email || !senha) {
    return res.status(400).json({ 
      success: false, 
      error: 'E-mail e senha são obrigatórios' 
    });
  }

  // Usuário padrão para autenticação do sistema Cerberus
  const adminEmail = process.env.ADMIN_EMAIL || 'admin@cerberus.com.br';
  const adminSenha = process.env.ADMIN_PASSWORD || 'admin123';

  if (email === adminEmail && senha === adminSenha) {
    return res.status(200).json({
      success: true,
      message: 'Autenticação realizada com sucesso',
      token: 'cerberus-auth-token-jwt-mock',
      user: {
        email,
        role: 'Administrator'
      }
    });
  }

  return res.status(401).json({ 
    success: false, 
    error: 'Credenciais inválidas' 
  });
};
