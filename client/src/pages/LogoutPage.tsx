import { useNavigate } from 'react-router-dom';
import { 
  LogOut, 
  CheckCircle,
  ArrowLeft,
  FlaskConical
} from 'lucide-react';

const LogoutPage = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-blue-50 flex flex-col">
      {/* Header */}
      <header className="py-6 px-6">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <div className="flex items-center gap-2">
            <FlaskConical className="w-7 h-7 text-blue-600" />
            <span className="text-xl font-bold text-slate-900">
              ChemVerify <span className="text-blue-600">AI</span>
            </span>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 flex flex-col items-center justify-center px-6 py-12">
        {/* Success Icon */}
        <div className="relative mb-8">
          <div className="w-24 h-24 bg-emerald-100 rounded-full flex items-center justify-center">
            <CheckCircle className="w-12 h-12 text-emerald-600" />
          </div>
          <div className="absolute -bottom-1 -right-1 w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center">
            <LogOut className="w-4 h-4 text-white" />
          </div>
        </div>

        {/* Message */}
        <h1 className="text-3xl md:text-4xl font-bold text-slate-900 text-center mb-4">
          You've Been Logged Out
        </h1>
        <p className="text-slate-600 text-center max-w-md mb-8">
          Your session has been securely ended. Thank you for using the Ingredient Intelligence Portal.
        </p>

        {/* Session Info Card */}
        <div className="bg-white border border-slate-200 rounded-xl p-6 mb-8 max-w-sm w-full">
          <h3 className="text-sm font-semibold text-slate-900 mb-4">Session Summary</h3>
          <div className="space-y-3">
            <div className="flex justify-between text-sm">
              <span className="text-slate-500">Session duration</span>
              <span className="text-slate-900 font-medium">45 minutes</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-slate-500">Analyses performed</span>
              <span className="text-slate-900 font-medium">12</span>
            </div>
            <div className="flex justify-between text-sm">
              <span className="text-slate-500">Last activity</span>
              <span className="text-slate-900 font-medium">Just now</span>
            </div>
          </div>
        </div>

        {/* Action Buttons */}
        <div className="flex flex-col sm:flex-row gap-4">
          <button 
            className="btn-primary"
            onClick={() => navigate('/login')}
          >
            Log In Again
          </button>
          <button 
            className="btn-secondary"
            onClick={() => navigate('/')}
          >
            <ArrowLeft className="w-4 h-4" />
            Return to Homepage
          </button>
        </div>

        {/* Security Notice */}
        <div className="mt-12 flex items-center gap-2 text-xs text-slate-400">
          <div className="w-2 h-2 bg-emerald-400 rounded-full"></div>
          <span>Your data has been securely saved and encrypted</span>
        </div>
      </main>

      {/* Footer */}
      <footer className="py-6 border-t border-slate-100">
        <div className="max-w-7xl mx-auto px-6 flex flex-col md:flex-row items-center justify-between gap-4">
          <span className="text-sm text-slate-500">
            © 2024 ChemVerify Systems Inc. All rights reserved.
          </span>
          <div className="flex items-center gap-6">
            <a href="#privacy" className="text-sm text-slate-500 hover:text-blue-600 transition-colors">
              Privacy Policy
            </a>
            <a href="#terms" className="text-sm text-slate-500 hover:text-blue-600 transition-colors">
              Terms of Service
            </a>
            <a href="#support" className="text-sm text-slate-500 hover:text-blue-600 transition-colors">
              Contact Support
            </a>
          </div>
        </div>
      </footer>
    </div>
  );
};

export default LogoutPage;
