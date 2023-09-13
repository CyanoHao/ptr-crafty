local _

_ = CreateFrame("Button", "CraftySendRuneButton")
_:SetScript("OnClick", function()
    for bag = 0, 5, 1 do
        for slot = 1, C_Container.GetContainerNumSlots(bag), 1 do
            local name = C_Container.GetContainerItemLink(bag,slot)
            if name and string.find(name, "Augment Rune") then
                C_Container.UseContainerItem(bag, slot)
            end
        end
    end
end)

_ = CreateFrame("Button", "CraftySendHammerButton")
_:SetScript("OnClick", function()
    for bag = 0, 5, 1 do
        for slot = 1, C_Container.GetContainerNumSlots(bag), 1 do
            local name = C_Container.GetContainerItemLink(bag,slot)
            if name and string.find(name, "Auto%-Hammer") then
                C_Container.UseContainerItem(bag, slot)
            end
        end
    end
end)

_ = CreateFrame("Button", "CraftySendGliderButton")
_:SetScript("OnClick", function()
    for bag = 0, 5, 1 do
        for slot = 1, C_Container.GetContainerNumSlots(bag), 1 do
            local name = C_Container.GetContainerItemLink(bag,slot)
            if name and string.find(name, "Goblin Glider Kit") then
                C_Container.UseContainerItem(bag, slot)
            end
        end
    end
end)
