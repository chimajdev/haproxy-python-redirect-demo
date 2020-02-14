local sleepSecs = 3

core.register_service("queueapp", "http", function(applet)
  core.msleep(sleepSecs * 1000)

  local url = applet.path .. "?"

  if applet.qs ~= "" then
    url = url .. applet.qs .. "&"
  end

  url = url .. "fromLua=true&appTalk=redirectFromSleep"

	applet:set_status(302)
	applet:add_header("location", url)
	applet:start_response()
	applet:send([[]])
end)
