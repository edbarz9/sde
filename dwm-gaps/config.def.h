/* See LICENSE file for copyright and license details. */

/* appearance */
static const unsigned int borderpx  = 0;        /* border pixel of windows */
static const unsigned int gappx     = 14;       /* gap pixel between windows */
static const unsigned int snap      = 32;       /* snap pixel */
static const int showbar            = 1;        /* 0 means no bar */
static const int topbar             = 1;        /* 0 means bottom bar */
static const char *fonts[]          = { "Envy Code R:size=12" };
static const char dmenufont[]       = "Envy Code R:size=12";
static const char col_gray1[]       = "#2d332d";
static const char col_gray2[]       = "#2d332d";
static const char col_gray3[]       = "#cbe6cb";
static const char col_gray4[]       = "#cbe6cb";
static const char col_cyan[]        = "#5ca77e";
static const char *colors[][3]      = {
	/*               fg         bg         border   */
	[SchemeNorm] = { col_gray3, col_gray1, col_gray2 },
	[SchemeSel]  = { col_gray1, col_cyan,  col_cyan  },
};

/* tagging */
static const char *tags[] = { "1", "2", "3", "4", "5", "6", "7", "8", "9" };

static const Rule rules[] = {
	/* xprop(1):
	 *	WM_CLASS(STRING) = instance, class
	 *	WM_NAME(STRING) = title
	 */
	/* class      instance    title       tags mask     isfloating   monitor */
	{ "pd",       NULL,       NULL,       0,            1,           -1 },
	/*{ "Gimp",     NULL,       NULL,       0,            1,           -1 },
	{ "Firefox",  NULL,       NULL,       1 << 8,       0,           -1 },*/
};

/* layout(s) */
static const float mfact     = 0.55; /* factor of master area size [0.05..0.95] */
static const int nmaster     = 1;    /* number of clients in master area */
static const int resizehints = 1;    /* 1 means respect size hints in tiled resizals */

static const Layout layouts[] = {
	/* symbol     arrange function */
	{ "T",      tile },
	{ "M",      monocle },
  { "D",      deck },
	{ "F",      NULL },
};

/* key definitions */
#define XF86AudioLowerVolume  0x1008ff11
#define XF86AudioRaiseVolume  0x1008ff13
#define XF86AudioMute         0x1008ff12
#define XF86AudioNext         0x1008ff17
#define XF86AudioPrev         0x1008ff16
#define XF86AudioPlay         0x1008ff14
#define XF86MonBrightnessUp   0x1008ff02
#define XF86MonBrightnessDown 0x1008ff03
#define Print                 0xff61
#define MODKEY Mod4Mask
#define TAGKEYS(KEY,TAG) \
	{ MODKEY,                       KEY,      view,           {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask,           KEY,      toggleview,     {.ui = 1 << TAG} }, \
	{ MODKEY|ShiftMask,             KEY,      tag,            {.ui = 1 << TAG} }, \
	{ MODKEY|ControlMask|ShiftMask, KEY,      toggletag,      {.ui = 1 << TAG} },

/* helper for spawning shell commands in the pre dwm-5.0 fashion */
#define SHCMD(cmd) { .v = (const char*[]){ "/bin/sh", "-c", cmd, NULL } }

/* commands */
static char dmenumon[2] = "0"; /* component of dmenucmd, manipulated in spawn() */
static const char *dmenucmd[] = { "dmenu_run", "-m", dmenumon, "-fn", dmenufont, "-nb", col_gray1, "-nf", col_gray3, "-sb", col_cyan, "-sf", col_gray1, NULL };
static const char *termcmd[]  = { "st-82", NULL };
static const char *poff[]  = { "poff", NULL };
static const char *muusb[]  = { "muusb", NULL };
static const char *volup[] = {"amixer","sset","Master","5%+",NULL };
static const char *voldown[] = {"amixer","sset","Master","5%-",NULL };
static const char *volmute[] = {"amixer","sset","Master","toggle",NULL };
static const char *lightmore[] = {"sudo","bcklght","+",NULL };
static const char *lightless[] = {"sudo","bcklght","-",NULL };
static const char *cmusnext[] = {"cmus-remote", "-n", NULL};
static const char *cmusprev[] = {"cmus-remote", "-r", NULL};
static const char *cmusplay[] = {"cmus-remote", "-u", NULL};
char *scrotshot[] = {"scrotshot", NULL};

static Key keys[] = {
	/* modifier                     key        function        argument */
	{ MODKEY,                       XK_p,      spawn,          {.v = dmenucmd } },
	{ MODKEY,                       XK_Return, spawn,          {.v = termcmd } },
	{ MODKEY,                       XK_b,      togglebar,      {0} },
	{ MODKEY,                       XK_k,      focusstack,     {.i = +1 } },
	{ MODKEY,                       XK_j,      focusstack,     {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_k,      incnmaster,     {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_j,      incnmaster,     {.i = -1 } },
	{ MODKEY,                       XK_h,      setmfact,       {.f = -0.05} },
	{ MODKEY,                       XK_l,      setmfact,       {.f = +0.05} },
	//{ MODKEY,                       XK_Return, zoom,           {0} },
	{ MODKEY,                       XK_Tab,    view,           {0} },
	{ MODKEY|ShiftMask,             XK_c,      killclient,     {0} },
	{ MODKEY,                       XK_t,      setlayout,      {.v = &layouts[0]} },
	{ MODKEY,                       XK_m,      setlayout,      {.v = &layouts[1]} },
	{ MODKEY,                       XK_d,      setlayout,      {.v = &layouts[2]} },
	{ MODKEY,                       XK_f,      setlayout,      {.v = &layouts[3]} },
	{ MODKEY,                       XK_space,  setlayout,      {0} },
	{ MODKEY|ShiftMask,             XK_space,  togglefloating, {0} },
	{ MODKEY,                       XK_0,      view,           {.ui = ~0 } },
	{ MODKEY|ShiftMask,             XK_0,      tag,            {.ui = ~0 } },
	{ MODKEY,                       XK_comma,  focusmon,       {.i = -1 } },
	{ MODKEY,                       XK_period, focusmon,       {.i = +1 } },
	{ MODKEY|ShiftMask,             XK_comma,  tagmon,         {.i = -1 } },
	{ MODKEY|ShiftMask,             XK_period, tagmon,         {.i = +1 } },
  /* custom commands */
	{ MODKEY,                       XK_o,      spawn,          {.v = poff } },
	{ MODKEY,                       XK_u,      spawn,          {.v = muusb } },
	{ MODKEY,                       XK_i,	     spawn,          {.v = scrotshot }},
	{ 0,			                      XF86MonBrightnessUp,	spawn, {.v = lightmore }},
	{ 0,			                      XF86MonBrightnessDown,spawn, {.v = lightless }},
	{ 0,			                      XF86AudioMute,	      spawn, {.v = volmute }},
	{ 0,			                      XF86AudioRaiseVolume, spawn, {.v = volup }},
	{ 0,			                      XF86AudioLowerVolume, spawn, {.v = voldown }},
	{ 0,			                      XF86AudioNext,        spawn, {.v = cmusnext }},
	{ 0,			                      XF86AudioPrev,        spawn, {.v = cmusprev }},
	{ 0,			                      XF86AudioPlay,        spawn, {.v = cmusplay }},
  TAGKEYS(                        XK_ampersand,              0)
  TAGKEYS(                        XK_eacute,                 1)
  TAGKEYS(                        XK_quotedbl,               2)
  TAGKEYS(                        XK_apostrophe,             3)
  TAGKEYS(                        XK_parenleft,              4)
  TAGKEYS(                        XK_section,                5)
  TAGKEYS(                        XK_egrave,                 6)
  TAGKEYS(                        XK_exclam,                 7)
  TAGKEYS(                        XK_ccedilla,               8)
	{ MODKEY|ShiftMask,             XK_q,      quit,           {0} },
};

/* button definitions */
/* click can be ClkTagBar, ClkLtSymbol, ClkStatusText, ClkWinTitle, ClkClientWin, or ClkRootWin */
static Button buttons[] = {
	/* click                event mask      button          function        argument */
	{ ClkLtSymbol,          0,              Button1,        setlayout,      {0} },
	{ ClkLtSymbol,          0,              Button3,        setlayout,      {.v = &layouts[2]} },
	{ ClkWinTitle,          0,              Button2,        zoom,           {0} },
	{ ClkStatusText,        0,              Button2,        spawn,          {.v = termcmd } },
	{ ClkClientWin,         MODKEY,         Button1,        movemouse,      {0} },
	{ ClkClientWin,         MODKEY,         Button2,        togglefloating, {0} },
	{ ClkClientWin,         MODKEY,         Button3,        resizemouse,    {0} },
	{ ClkTagBar,            0,              Button1,        view,           {0} },
	{ ClkTagBar,            0,              Button3,        toggleview,     {0} },
	{ ClkTagBar,            MODKEY,         Button1,        tag,            {0} },
	{ ClkTagBar,            MODKEY,         Button3,        toggletag,      {0} },
};

