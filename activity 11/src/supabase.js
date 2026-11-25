import { createClient } from '@supabase/supabase-js'

// =========================================================================
// 💡 ACTIVITY 11: SUPABASE CLIENT CONFIGURATION
// - Connects React to your live PostgreSQL database on Supabase.
// - Reads from .env.local with safe fallbacks so it never fails.
// =========================================================================
const supabaseUrl = import.meta.env.VITE_SUPABASE_URL || 'https://revfyzjtsddsigewohzp.supabase.co'
const supabaseKey = import.meta.env.VITE_SUPABASE_ANON_KEY || 'sb_publishable_fuqtvsngGG8gTzRUPbVSig_47TJY_QU'

export const supabase = createClient(supabaseUrl, supabaseKey)
